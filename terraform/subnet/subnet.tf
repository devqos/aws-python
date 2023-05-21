variable "vpc_id" {
  description = "VPC ID"
}

variable "cidr_block" {
  description = "CIDR Block"
}

variable "is_public" {
  description = "Is public resource?"
}

variable "availability_zone" {
  description = "Availability zone"
}

variable "tag_name" {
  description = "Tag name"
}

resource "aws_subnet" "subnet" {
  vpc_id                  = var.vpc_id
  cidr_block              = var.cidr_block
  availability_zone       = var.availability_zone
  map_public_ip_on_launch = var.is_public

  tags = {
    Name = var.tag_name
  }
}

output "subnet_id" {
  value = aws_subnet.subnet.id
}