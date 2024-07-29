import UnitList from "@pages/UnitList";
import UnitForm from "./UnitForm";
import { useEffect, useState } from "react";
import { Unit as IUnit } from "src/types";
import { getUnits } from "@services/units";
import { useCommandDialog } from "@providers/index";
import { HiOutlinePlus as NewIcon } from "react-icons/hi2"

export default function Unit() {

    const [data, setData] = useState<Array<IUnit>>([]);

    const {
        showCommandDialog,
    } = useCommandDialog();

    useEffect(() => {

        const fetchData = async () => {
            const units = await getUnits();
            setData(units)
        }

        fetchData();


    })


    return <div id='Unit' className="">
        <div className="flex flex-row-reverse">
            <button onClick={() => showCommandDialog(<UnitForm />)}
                className="flex items-center gap-x-2 bg-blue-500 text-white p-2 rounded"
            >
                <NewIcon size={18} />
                <span>Add Unit</span>
            </button>
        </div>
        <UnitList data={data} />
    </div>
}