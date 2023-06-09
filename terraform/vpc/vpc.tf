resource "aws_vpc" "vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "s3uploader-vpc"
  }
}

output "vpc_id" {
  value = aws_vpc.vpc.id
}