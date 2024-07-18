import StaffList  from "@pages/StaffList"
import { getStaffs } from "@services/staffs";
import { useEffect, useState } from "react";
import { Staff as IStaff } from "@types/index";


export default function Staff() {

	const [data, setData] = useState<Array<IStaff>>([]);

	useEffect(() => {

		const fetchData = async () => {
			const staffs = await getStaffs();
			setData(staffs)
		}

		fetchData();

	}, [])

	return (
		<div className="">
			<StaffList data={data}/>
		</div>)
}