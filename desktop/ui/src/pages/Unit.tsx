import UnitList from "@pages/UnitList";
import { useEffect, useState } from "react";
import { Unit as IUnit } from "src/types/index";
import { getUnits } from "@services/units";

export default function Unit() {

    const [data, setData] = useState<Array<IUnit>>([]);

    useEffect(() => {

        const fetchData = async () => {
            const units = await getUnits();
            setData(units)
        }

        fetchData();

    }, [])


    return <div id='Unit' className="">
        <UnitList data={data} />
    </div>
}