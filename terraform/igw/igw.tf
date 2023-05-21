variable "vpc_id" {
  description = "VPC ID"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = var.vpc_id

  tags = {
    Name = "s3uploader-igw"
  }
}

output "igw_id" {
  value = aws_internet_gateway.igw.id
}