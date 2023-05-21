variable "vpc_id" {
  description = "VPC ID"
}

variable "is_public" {
  description = "Is public resource?"
}

variable "tag_name" {
  description = "Tag name"
}

variable "igw_id" {
  description = "IGW ID"
  default     = null
}

resource "aws_route_table" "rt" {
  vpc_id = var.vpc_id

  dynamic "route" {
    for_each = var.is_public ? [1] : []
    content {
      cidr_block = "0.0.0.0/0"
      gateway_id = var.igw_id
    }
  }

  tags = {
    Name = var.tag_name
  }
}

output "route_table_id" {
  value = aws_route_table.rt.id
}