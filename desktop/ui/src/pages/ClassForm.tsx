import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { newClass } from '@/services/classes';

// Define the zod schema
const classSchema = z.object({
    classId: z.string().nonempty({ message: 'Class ID is required' }),
    classRep: z.string().nonempty({ message: 'Class Rep is required' })
});

type ClassRep = z.infer<typeof classSchema>;


export default function ClassRepForm() {

    const { register, handleSubmit, formState: { errors }, reset } = useForm<ClassRep>({
        resolver: zodResolver(classSchema),
    });

    const onSubmit = (data: ClassRep) => {

        if (!newClass(data)) {
            return;
        }

        reset();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="my-2 px-2 space-y-4">
            <div className="">
                <h2>CLASS REGISTRATION</h2>
            </div>
            <div>
                <label htmlFor="regNo">Reg No</label>
                <input
                    id="classId"
                    type="text"
                    {...register('classId')}
                    className="border p-2 rounded w-full"
                />
                {errors.classId && <span className="text-red-600">{errors.classId.message}</span>}
            </div>
            <div>
                <label htmlFor="classRep">Class Rep</label>
                <input
                    id="classRep"
                    type="text"
                    {...register('classRep')}
                    className="border p-2 rounded w-full"
                />
                {errors.classRep && <span className="text-red-600">{errors.classRep.message}</span>}
            </div>

            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Submit
            </button>
        </form>
    );
}