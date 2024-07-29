import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { newClassRep } from '@services/classreps'

// Define the zod schema
const unitSchema = z.object({
    regNo: z.string().nonempty({ message: 'Registration Number is required' }),
    firstName: z.string().nonempty({ message: 'FirstName is required' }),
    middleName: z.string().nonempty({ message: 'Middle is required' }),
    lastName: z.string().nonempty({ message: 'LastName is required' }),
    mobileNo: z.string().nonempty({ message: 'Mobile number is required' }),
    email: z.string().nonempty({ message: 'Email address is required' })
});

type ClassRep = z.infer<typeof unitSchema>;


export default function ClassRepForm() {

    const { register, handleSubmit, formState: { errors }, reset } = useForm<ClassRep>({
        resolver: zodResolver(unitSchema),
    });

    const onSubmit = (data: ClassRep) => {

        if (!newClassRep(data)) {
            return;
        }

        reset();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="my-2 px-2 space-y-4">
            <div className="">
                <h2>UNIT REGISTRATION</h2>
            </div>
            <div>
                <label htmlFor="regNo">Reg No</label>
                <input
                    id="regNo"
                    type="text"
                    {...register('regNo')}
                    className="border p-2 rounded w-full"
                />
                {errors.regNo && <span className="text-red-600">{errors.regNo.message}</span>}
            </div>

            <div>
                <label htmlFor="firstName">First Name</label>
                <input
                    id="firstName"
                    type="text"
                    {...register('firstName')}
                    className="border p-2 rounded w-full"
                />
                {errors.firstName && <span className="text-red-600">{errors.firstName.message}</span>}
            </div>
            <div>
                <label htmlFor="middleName">Middle Name</label>
                <input
                    id="middleName"
                    type="text"
                    {...register('middleName')}
                    className="border p-2 rounded w-full"
                />
                {errors.middleName && <span className="text-red-600">{errors.middleName.message}</span>}
            </div>
            <div>
                <label htmlFor="lastName">Last Name</label>
                <input
                    id="lastName"
                    type="text"
                    {...register('lastName')}
                    className="border p-2 rounded w-full"
                />
                {errors.lastName && <span className="text-red-600">{errors.lastName.message}</span>}
            </div>
            <div>
                <label htmlFor="email">Email</label>
                <input
                    id="email"
                    type="text"
                    {...register('email')}
                    className="border p-2 rounded w-full"
                />
                {errors.email && <span className="text-red-600">{errors.email.message}</span>}
            </div>
            <div>
                <label htmlFor="mobileNo">Phone</label>
                <input
                    id="mobileNo"
                    type="text"
                    {...register('mobileNo')}
                    className="border p-2 rounded w-full"
                />
                {errors.mobileNo && <span className="text-red-600">{errors.mobileNo.message}</span>}
            </div>

            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Submit
            </button>
        </form>
    );
}