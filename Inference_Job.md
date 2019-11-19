## Inference Platform
##### 1.Get data
```
context.list
2002:6009:O1-Power<>2002:6012:O1-Voltage<>2002:6015:O1-Current<>2002:6002:O1-Temp-a<>2002:6003:O1-Temp-b
2002:6002:O1-Temp-a<>2002:6009:O1-Power<>2002:6012:O1-Voltage<>2002:6015:O1-Current
2002:6002:O1-Temp-a<>2002:6009:O1-Power<>2002:6012:O1-Voltage<>2002:6015:O1-Current
"$.Oven_1_0000094147_1.row_id"
"$.Oven_1_0000094147_1.metadata.0.node_id"


String row_node = input_row.oven1_row_id_temp + ":" + input_row.oven1_node_id_temp + ":" + input_row.oven1_mes_name_temp;
if (context.list.isEmpty()) {
	context.list = row_node;
} else if (!context.list.contains(row_node)) {
	context.list += "<>" + row_node;
}
output_row.oven1_row_id_temp = input_row.oven1_row_id_temp;
output_row.oven1_node_id_temp = input_row.oven1_node_id_temp;
output_row.oven1_mes_name_temp = input_row.oven1_mes_name_temp;
System.out.println(context.list);
```