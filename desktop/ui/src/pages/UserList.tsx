import { Table, TableColumnsType } from "antd";
import { User } from "src/types";


const columns: TableColumnsType<User> = [
    {
        title: "UserName",
        dataIndex: "userName"
    },
    {
        title: "Staff No",
        dataIndex: "staffNo"
    },
    {
        title: "Roles",
        dataIndex: "roles"
    }
];


export default function UserList({ data }: { data: Array<User> }) {


    const users = data;

    users.map((user) =>
        Object.assign(user, { key: user.userName }),
    );

    return (
        <Table columns={columns} dataSource={users} />);
}