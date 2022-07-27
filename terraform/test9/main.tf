locals {
	map1 = { a = "a" }
	map2 = merge({ b = "b" }, local.map1)
}

output test {
	value = local.map2
}
