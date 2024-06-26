terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.33.0"
    }
  }
}

provider "google" {
  project     = var.gcp_project_id
  region      = var.gcp_region
  credentials = "./key.json"
}

// Create a secret containing the personal access token and grant permissions to the Service Agent
resource "google_secret_manager_secret" "github_token_secret" {
  project   = var.gcp_project_id
  secret_id = "github_pat"

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "github_token_secret_version" {
  secret      = google_secret_manager_secret.github_token_secret.id
  secret_data = var.git_secret_token_data
}

data "google_iam_policy" "serviceagent_secretAccessor" {
  binding {
    role    = "roles/secretmanager.secretAccessor"
    members = [var.gcp_iam_role_member]
  }
}

resource "google_secret_manager_secret_iam_policy" "policy" {
  project     = google_secret_manager_secret.github_token_secret.project
  secret_id   = google_secret_manager_secret.github_token_secret.secret_id
  policy_data = data.google_iam_policy.serviceagent_secretAccessor.policy_data
}

// Create the GitHub connection for note-app-backend
resource "google_cloudbuildv2_connection" "github_connection" {
  project  = var.gcp_project_id
  location = var.gcp_region
  name     = "github_connection"

  github_config {
    app_installation_id = var.git_app_install_id
    authorizer_credential {
      oauth_token_secret_version = google_secret_manager_secret_version.github_token_secret_version.id
    }
  }
  depends_on = [google_secret_manager_secret_iam_policy.policy]
}

// Create the GitHub connection for note-app-frontend-react
resource "google_cloudbuildv2_connection" "github_connection_frontend_react" {
  project  = var.gcp_project_id
  location = var.gcp_region
  name     = "github_connection_front_react"

  github_config {
    app_installation_id = var.git_app_install_id
    authorizer_credential {
      oauth_token_secret_version = google_secret_manager_secret_version.github_token_secret_version.id
    }
  }
  depends_on = [google_secret_manager_secret_iam_policy.policy]
}

resource "google_cloudbuildv2_repository" "note_repository" {
  project           = var.gcp_project_id
  location          = var.gcp_region
  name              = "note-rest-api2"
  parent_connection = google_cloudbuildv2_connection.github_connection.name
  remote_uri        = var.git_uri
}

resource "google_cloudbuildv2_repository" "note_repository_react" {
  project           = var.gcp_project_id
  location          = var.gcp_region
  name              = "note-app-react"
  parent_connection = google_cloudbuildv2_connection.github_connection_frontend_react.name
  remote_uri        = var.git_uri_front_react
}


resource "google_cloudbuild_trigger" "note_app_backend_trigger" {
  location = var.gcp_region
  name     = "note-app-backend"
  filename = "cloudbuild.yaml"
  project  = var.gcp_project_id
  //service_account = var.gcp_cloud_build_service_account
  repository_event_config {
    repository = google_cloudbuildv2_repository.note_repository.id
    push {
      branch = "^test$"
    }
  }
}

resource "google_cloudbuild_trigger" "note_app_front_react_trigger" {
  location = var.gcp_region
  name     = "note-app-react"
  filename = "cloudbuild.yaml"
  project  = var.gcp_project_id
  //service_account = var.gcp_cloud_build_service_account
  repository_event_config {
    repository = google_cloudbuildv2_repository.note_repository_react.id
    push {
      branch = "^test$"
    }
  }
}