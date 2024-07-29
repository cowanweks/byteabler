import ClassForm from "./ClassForm";
import { useEffect, useState } from "react";
import { Class as IClass } from "src/types";
import { useCommandDialog } from "@providers/index";
import { HiOutlinePlus as NewIcon } from "react-icons/hi2"
import { getClasses } from "@/services/classes";
import ClassList from "./ClassList";

export default function Class() {

    const [data, setData] = useState<Array<IClass>>([]);

    const {
        showCommandDialog,
    } = useCommandDialog();

    useEffect(() => {

        const fetchData = async () => {
            const classes = await getClasses();
            setData(classes)
        }

        fetchData();

    })


    return <div id='Class' className="">
        <div className="flex flex-row-reverse">
            <button onClick={() => showCommandDialog(<ClassForm />)}
                className="flex items-center gap-x-2 bg-blue-500 text-white p-2 rounded"
            >
                <NewIcon size={18} />
                <span>New Class</span>
            </button>
        </div>
        <ClassList data={data} />
    </div>
}