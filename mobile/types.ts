// export const API_URL = "http://127.0.0.1:3000/api/v1";
export const API_URL = "https://byteabler-8c063875d0ca.herokuapp.com/api/v1/";

export type Role = {
  roleID: string;
  role: string;
};

export type User = {
  userId: string;
  username: string;
  password: string;
  roles: Array<Role>;
};

export type Staff = {
  staffNo: string;
  firstName: string;
  middleName: string;
  lastName: string;
  natId: string;
  mobileNo: string;
  email: string;
  dateofBirth: Date;
};

export interface Lecturer extends Staff {}

export type Unit = {
  unitCode: string;
  unitName: string;
};

export type ClassRep = {
  regNo: string;
  firstName: string;
  middleName: string;
  lastName: string;
  mobileNo: string;
  email: string;
};

export type Class = {
  classID: string;
  year: number;
  semester: number;
  ClassRep: ClassRep;
};