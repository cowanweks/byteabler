import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { newLecture } from '@services/lectures';
import { useToast } from "@providers/index";
import { useEffect, useState } from 'react';
import { getUnits } from '@/services/units';
import { getStaffs } from '@/services/staffs';
import { Unit, Staff } from '@/types';

// Define the zod schema
const lectureSchema = z.object({
    classId: z.string().nonempty({ message: 'Class ID is required' }),
    unitCode: z.string().nonempty({ message: 'Unit Code is required' }),
    lecturer: z.string().nonempty({ message: 'Staff No is required' }),
    weekDay: z.string().nonempty({ message: 'Lecture Day is required' }),
    time: z.string().nonempty({ message: 'Lecture time is required' })
});

type Lecture = z.infer<typeof lectureSchema>;

export default function LectureForm() {
    const [units, setUnits] = useState<Unit[]>([]);
    const [staffs, setStaffs] = useState<Staff[]>([]);
    const { showToast } = useToast();
    const { register, handleSubmit, formState: { errors }, reset } = useForm<Lecture>({
        resolver: zodResolver(lectureSchema),
    });


    useEffect(() => {

        const fetchUnits = async () => {

            const response = await getUnits();

            setUnits(response)
        }

        const fetchStaffs = async () => {

            const response = await getStaffs();

            setStaffs(response)
        }

        fetchUnits()
        fetchStaffs()

    })

    const onSubmit = async (data: Lecture) => {

        const response = await newLecture(data);

        if (response.status === 400) {
            showToast('error', "Please make sure all fields are provided and in the required format");
            return;
        }

        showToast('success', response.msg);
        reset();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="my-2 px-2 space-y-4">
            <div className="">
                <h2>LECTURE REGISTRATION</h2>
            </div>
            <div>
                <label htmlFor="classId">Class ID</label>
                <input
                    id="classId"
                    type="text"
                    {...register('classId')}
                    className="border p-2 rounded w-full"
                />
                {errors.classId && <span className="text-red-600">{errors.classId.message}</span>}
            </div>
            <div>
                <label htmlFor="unitCode">Unit Code</label>
                <select
                    id="unitCode"
                    {...register('unitCode')}
                    className="border p-2 rounded w-full"
                >
                    <option value="">Select Unit</option>
                    {units.map((unit) =>
                        <option key={unit.unitCode} value={unit.unitCode}>{unit.unitCode}</option>
                    )}
                </select>
                {errors.unitCode && <span className="text-red-600">{errors.unitCode.message}</span>}
            </div>
            <div>
                <label htmlFor="lecturer">Lecturer</label>
                <select
                    id="lecturer"
                    {...register('lecturer')}
                    className="border p-2 rounded w-full"
                >
                    <option value="">Select Lecturer</option>
                    {staffs.map((staff) =>
                        <option key={staff.staffNo} value={staff.staffNo}>{staff.staffNo}</option>
                    )}
                </select>
                {errors.lecturer && <span className="text-red-600">{errors.lecturer.message}</span>}
            </div>
            <div>
                <label htmlFor="weekDay">Day</label>
                <select
                    id="weekDay"
                    {...register('weekDay')}
                    className="border p-2 rounded w-full"
                >
                    <option value="">Select Lecture Day</option>
                    <option value="Monday">Monday</option>
                    <option value="Tuesday">Tuesday</option>
                    <option value="Wednesday">Wednesday</option>
                    <option value="Thursday">Thursday</option>
                    <option value="Friday">Friday</option>
                    <option value="Saturday">Monday</option>
                    <option value="Sunday">Sunday</option>
                </select>
                {errors.weekDay && <span className="text-red-600">{errors.weekDay.message}</span>}
            </div>
            <div>
                <label htmlFor="time">Time</label>
                <input
                    id="time"
                    type="text"
                    {...register('time')}
                    placeholder="e.g., 8:00"
                    className="border p-2 rounded w-full"
                />
                {errors.time && <span className="text-red-600">{errors.time.message}</span>}
            </div>
            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Submit
            </button>
        </form>
    );
}
