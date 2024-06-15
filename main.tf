terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 4.0.0"
    }
  }
}

provider "google" {
  project = "note-app-426513"
  region = "europe-north1"
  credentials = "./key.json"
}

resource "google_cloudbuild_trigger" "include-build-logs-trigger" {
  location = "europe-north1"
  name     = "note-app-backend"
  filename = "cloudbuild.yaml"

  github {
    owner = "Olujuwon"
    name  = "note-rest-api"
    push {
      branch = "^test$"
    }
  }

}