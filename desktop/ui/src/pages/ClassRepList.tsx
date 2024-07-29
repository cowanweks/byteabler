import { Table, TableColumnsType } from "antd";
import { ClassRep } from "src/types";


const columns: TableColumnsType<ClassRep> = [
    {
        title: "Reg No",
        dataIndex: "regNo"
    },
    {
        title: "First Name",
        dataIndex: "firstName"
    },
    {
        title: "Middle Name",
        dataIndex: "middleName"
    },
    {
        title: "Last Name",
        dataIndex: "lastName"
    },
    {
        title: "Mobile",
        dataIndex: "mobileNo"
    },
    {
        title: "Email",
        dataIndex: "email"
    }
];


export default function ClassRepList({ data }: { data: Array<ClassRep> }) {



    const classreps = data;

    classreps.map((classrep) =>
        Object.assign(classrep, { key: classrep.regNo }),
    );

    return (
        <Table columns={columns} dataSource={classreps} />);
}