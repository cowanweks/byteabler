import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { newUser } from '@/services/users';
import {useToast} from "@providers/index"

// Define the zod schema
const classSchema = z.object({

  staffNo: z.string().nonempty({ message: 'Staff No ID is required' }),
  userName: z.string().nonempty({ message: 'UserName ID is required' }),
  password: z.string().nonempty({ message: 'Password is required' }),
  confirmPassword: z.string().nonempty({ message: 'Role is required' }),
  roles: z.string().nonempty({ message: 'Role is required' })
});

type User = z.infer<typeof classSchema>;


export default function UserForm() {

    const {showToast} = useToast()


    const { register, handleSubmit, formState: { errors }, reset } = useForm<User>({
        resolver: zodResolver(classSchema),
    });

    const onSubmit = async (data: User) => {

        const response = await newUser(data);

        if(response.status == 409){

            showToast('error', "A User with this userName or Staff No already exists!");

            return;
        }

        showToast('success', "Successfully Added a new User!");

        reset();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="my-2 px-2 space-y-4">
            <div className="">
                <h2>USER REGISTRATION</h2>
            </div>
            <div>
                <label htmlFor="staffNo">Staff No</label>
                <input
                    id="staffNo"
                    type="text"
                    {...register('staffNo')}
                    placeholder='Staff No'
                    className="border p-2 rounded w-full"
                />
                {errors.staffNo && <span className="text-red-600">{errors.staffNo.message}</span>}
            </div>
            <div>
                <label htmlFor="userName">User Name</label>
                <input
                    id="userName"
                    type="text"
                    {...register('userName')}
                    placeholder='UserName'
                    className="border p-2 rounded w-full"
                />
                {errors.userName && <span className="text-red-600">{errors.userName.message}</span>}
            </div>
            <div>
                <label htmlFor="password">Password</label>
                <input
                    id="password"
                    type="password"
                    {...register('password')}
                    placeholder='Password'
                    className="border p-2 rounded w-full"
                />
                {errors.password && <span className="text-red-600">{errors.password.message}</span>}
            </div>
            <div>
                <label htmlFor="confirmPassword">Confirm Password</label>
                <input
                    id="confirmPassword"
                    type="password"
                    {...register('confirmPassword')}
                    placeholder='Password'
                    className="border p-2 rounded w-full"
                />
                {errors.confirmPassword && <span className="text-red-600">{errors.confirmPassword.message}</span>}
            </div>

            <div>
                <label htmlFor="roles">Roles</label>
                <input
                    id="roles"
                    type="text"
                    {...register('roles')}
                    placeholder='Roles'
                    className="border p-2 rounded w-full"
                />
                {errors.roles && <span className="text-red-600">{errors.roles.message}</span>}
            </div>

            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Submit
            </button>
        </form>
    );
}