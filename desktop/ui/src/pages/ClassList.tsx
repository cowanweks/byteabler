import { Table, TableColumnsType } from "antd";
import { Class } from "src/types";


const columns: TableColumnsType<Class> = [
    {
        title: "Class ID",
        dataIndex: "classId"
    },
    {
        title: "Class Rep",
        dataIndex: "classRep"
    },
];


export default function ClassList({ data }: { data: Array<Class> }) {



    const classes = data;

    classes.map((_class) =>
        Object.assign(_class, { key: _class.classId }),
    );

    return (
        <Table columns={columns} dataSource={classes} />);
}