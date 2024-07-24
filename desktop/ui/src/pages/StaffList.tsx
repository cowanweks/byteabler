import { Table, TableColumnsType } from "antd";
import { Staff } from "src/types";


const columns: TableColumnsType<Staff> = [
	{
		title: "Staff No",
		dataIndex: "staffNo"
	},
	{
		title: "first Name",
		dataIndex: "firstName"
	}
];


export default function StaffList({ data }: { data: Array<Staff> }) {



	const staffs = data;

	staffs.map((staff) =>
		Object.assign(staff, { key: staff.staffNo }),
	);

	return (
		<Table columns={columns} dataSource={staffs} />);
}