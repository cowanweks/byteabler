import { Table, TableColumnsType } from "antd";
import { Lecture } from "src/types";


const columns: TableColumnsType<Lecture> = [
    {
        title: "Class ID",
        dataIndex: "classId"
    },
    {
        title: "Unit Code",
        dataIndex: "unitCode"
    },
    {
        title: "Unit Name",
        dataIndex: "unitName"
    },
    {
        title: "Lecturer",
        dataIndex: "lecturer"
    },
    {
        title: "Day",
        dataIndex: "weekDay"
    },
    {
        title: "Time",
        dataIndex: "time"
    }
];


export default function LectureList({ data }: { data: Array<Lecture> }) {



    const lectures = data;

    lectures.map((lecture) =>
        Object.assign(lecture, { key: lecture.lectureId }),
    );

    return (
        <Table columns={columns} dataSource={lectures} />);
}