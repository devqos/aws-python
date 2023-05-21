terraform {
  backend "s3" {
    bucket = "devqos-terraform-state"
    key    = "terraform/s3uploader-state"
    region = "eu-central-1"
  }
}