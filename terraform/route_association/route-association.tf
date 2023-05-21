variable "subnet_ids" {
  type        = list(string)
  description = "Subnet ID"
}

variable "route_table_id" {
  description = "RT ID"
}

resource "aws_route_table_association" "route_table_association" {
  count          = length(var.subnet_ids)
  subnet_id      = var.subnet_ids[count.index]
  route_table_id = var.route_table_id
}