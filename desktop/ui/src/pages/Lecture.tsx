import LectureList from "@pages/LectureList";
import LectureForm from "./LectureForm";
import { useEffect, useState } from "react";
import { Lecture as ILecture } from "src/types";
import { getLectures } from "@services/lectures";
import { useCommandDialog } from "@providers/index";
import { HiOutlinePlus as NewIcon } from "react-icons/hi2"

export default function Lecture() {

    const [data, setData] = useState<Array<ILecture>>([]);

    const {
        showCommandDialog,
    } = useCommandDialog();

    useEffect(() => {

        const fetchData = async () => {
            const lectures = await getLectures();
            setData(lectures)
        }

        fetchData();


    })


    return <div id='Unit' className="">
        <div className="flex flex-row-reverse">
            <button onClick={() => showCommandDialog(<LectureForm />)}
                className="flex items-center gap-x-2 bg-blue-500 text-white p-2 rounded"
            >
                <NewIcon size={18} />
                <span>Add Lecture</span>
            </button>
        </div>
        <LectureList data={data} />
    </div>
}