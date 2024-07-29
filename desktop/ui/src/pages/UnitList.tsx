import { Table, TableColumnsType } from "antd";
import { Unit } from "src/types";


const columns: TableColumnsType<Unit> = [
	{
		title: "Unit Code",
		dataIndex: "unitCode"
	},
	{
		title: "Unit Name",
		dataIndex: "unitName"
	}
];


export default function UnitList({ data }: { data: Array<Unit> }) {



	const units = data;

	units.map((unit) =>
		Object.assign(unit, { key: unit.unitCode }),
	);

	return (
		<Table columns={columns} dataSource={units} />);
}