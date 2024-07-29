import UserForm from "./UserForm";
import { useEffect, useState } from "react";
import { User as IUser } from "src/types";
import { useCommandDialog } from "@providers/index";
import { HiOutlinePlus as NewIcon } from "react-icons/hi2"
import { getUsers } from "@/services/users";
import UserList from "./UserList";

export default function Setting() {

    const [data, setData] = useState<Array<IUser>>([]);

    const {
        showCommandDialog,
    } = useCommandDialog();

    useEffect(() => {

        const fetchData = async () => {
            const users = await getUsers();
            setData(users)
        }

        fetchData();

    })


    return <div id='Class' className="">
        <div className="flex flex-row-reverse">
            <button onClick={() => showCommandDialog(<UserForm />)}
                className="flex items-center gap-x-2 bg-blue-500 text-white p-2 rounded"
            >
                <NewIcon size={18} />
                <span>New User</span>
            </button>
        </div>
        <UserList data={data} />
    </div>
}