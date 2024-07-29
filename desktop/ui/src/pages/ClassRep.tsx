import ClassRepFrom from "./ClassRepForm";
import { useEffect, useState } from "react";
import { ClassRep as IClassRep } from "src/types";
import { useCommandDialog } from "@providers/index";
import { HiOutlinePlus as NewIcon } from "react-icons/hi2"
import { getClassReps } from "@/services/classreps";
import ClassRepList from "./ClassRepList";

export default function ClassRep() {

    const [data, setData] = useState<Array<IClassRep>>([]);

    const {
        isOpen,
        showCommandDialog,
        hideCommandDialog
    } = useCommandDialog();

    useEffect(() => {

        const fetchData = async () => {
            const classreps = await getClassReps();
            setData(classreps)
        }

        fetchData();

    })


    return <div id='Unit' className="">
        <div className="flex flex-row-reverse">
            <button onClick={() => showCommandDialog(<ClassRepFrom />)}
                className="flex items-center gap-x-2 bg-blue-500 text-white p-2 rounded"
            >
                <NewIcon size={18} />
                <span>Add Rep</span>
            </button>
        </div>
        <ClassRepList data={data} />
    </div>
}