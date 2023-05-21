module "vpc" {
  source = "./vpc"
}

module "public_subnet_1a" {
  source            = "./subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = "10.0.0.0/20"
  availability_zone = "eu-central-1a"
  is_public         = true
  tag_name          = "public-1a"
}

module "public_subnet_1b" {
  source            = "./subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = "10.0.16.0/20"
  availability_zone = "eu-central-1b"
  is_public         = true
  tag_name          = "public-1b"
}

module "private_subnet_1a" {
  source            = "./subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = "10.0.32.0/20"
  availability_zone = "eu-central-1a"
  is_public         = false
  tag_name          = "private-1a"
}

module "private_subnet_1b" {
  source            = "./subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = "10.0.48.0/20"
  availability_zone = "eu-central-1b"
  is_public         = false
  tag_name          = "private-1b"
}

module "igw" {
  source = "./igw"
  vpc_id = module.vpc.vpc_id
}

module "public-route-table" {
  source    = "./route_table"
  vpc_id    = module.vpc.vpc_id
  is_public = true
  igw_id    = module.igw.igw_id
  tag_name  = "public-rt"
}

module "private-route-table" {
  source    = "./route_table"
  vpc_id    = module.vpc.vpc_id
  is_public = false
  igw_id    = module.igw.igw_id
  tag_name  = "private-rt"
}

module "public-rt-association" {
  source         = "./route_association"
  subnet_ids     = [module.public_subnet_1a.subnet_id, module.public_subnet_1b.subnet_id]
  route_table_id = module.public-route-table.route_table_id
}

module "private-rt-association" {
  source         = "./route_association"
  subnet_ids     = [module.private_subnet_1a.subnet_id, module.private_subnet_1b.subnet_id]
  route_table_id = module.private-route-table.route_table_id
}