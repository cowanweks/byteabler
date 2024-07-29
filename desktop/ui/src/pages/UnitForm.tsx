import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { newUnit } from '@services/units'

// Define the zod schema
const unitSchema = z.object({
    unitCode: z.string().nonempty({ message: 'Unit Code is required' }),
    unitName: z.string().nonempty({ message: 'Unit Name is required' }),
});

type Unit = z.infer<typeof unitSchema>;


export default function UnitForm() {

    const { register, handleSubmit, formState: { errors }, reset } = useForm<Unit>({
        resolver: zodResolver(unitSchema),
    });

    const onSubmit = (data: Unit) => {

        if (!newUnit(data)) {
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
                <label htmlFor="unitCode">Unit Code</label>
                <input
                    id="unitCode"
                    type="text"
                    {...register('unitCode')}
                    className="border p-2 rounded w-full"
                />
                {errors.unitCode && <span className="text-red-600">{errors.unitCode.message}</span>}
            </div>

            <div>
                <label htmlFor="unitName">Unit Name</label>
                <input
                    id="unitName"
                    type="text"
                    {...register('unitName')}
                    className="border p-2 rounded w-full"
                />
                {errors.unitName && <span className="text-red-600">{errors.unitName.message}</span>}
            </div>

            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Submit
            </button>
        </form>
    );
}