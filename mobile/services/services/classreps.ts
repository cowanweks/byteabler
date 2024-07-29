import { API_URL, ClassRep } from "../types";

export async function getClassReps(): Promise<Array<ClassRep>> {
  /**
   *
   */
  const response = await fetch(`${API_URL}/v1/classreps`, { method: "GET" });

  if (response.status != 200) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<ClassRep> = await response.json();

  return data;
}

export async function getClassRepByRegNo(regNo: string): Promise<ClassRep> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<ClassRep>}
   */
  const data: Array<ClassRep> = await getClassReps();

  const filteredData = data.filter((data) => data.regNo == regNo);

  return filteredData[0];
}

export async function newClassRep(classRepData: ClassRep): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {ClassRep} classRepData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (classRepData.regNo != null) form.append("regNo", classRepData.regNo);
  if (classRepData.firstName != null)
    form.append("firstName", classRepData.firstName);
  if (classRepData.middleName != null)
    form.append("middleName", classRepData.middleName);
  if (classRepData.lastName != null)
    form.append("lastName", classRepData.lastName);
  if (classRepData.email != null) form.append("email", classRepData.email);
  if (classRepData.mobileNo != null)
    form.append("mobileNo", classRepData.mobileNo);

  const response = await fetch(`${API_URL}/v1/classreps`, {
    method: "POST",
    body: form,
  });

  if (response.status != 201) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function updateClassRep(
  regNo: string,
  classRepData: Partial<ClassRep>
): Promise<boolean> {
  /**
   * @export
   * @param {string} regNo
   * @param {Partial<ClassRep>} classRepData
   * @return {*} {Promise<boolean>}
   */
  const form = new FormData();

  if (classRepData.firstName != null)
    form.append("firstName", classRepData.firstName);
  if (classRepData.middleName != null)
    form.append("middleName", classRepData.middleName);
  if (classRepData.lastName != null)
    form.append("lastName", classRepData.lastName);
  if (classRepData.email != null) form.append("email", classRepData.email);
  if (classRepData.mobileNo != null)
    form.append("mobileNo", classRepData.mobileNo);

  const response = await fetch(`${API_URL}/v1/classreps?regNo=${regNo}`, {
    method: "PUT",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteClassRep(regNo: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} regNo
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/classreps?regNo=${regNo}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
