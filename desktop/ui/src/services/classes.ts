import { API_URL, Class } from "../types";

export async function getClasses(): Promise<Array<Class>> {
  /**
   *
   */
  const response = await fetch(`${API_URL}/v1/classes`, { method: "GET" });

  if (response.status != 200) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<Class> = await response.json();

  return data;
}

export async function getClassById(classId: string): Promise<Class> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<Class>}
   */
  const data: Array<Class> = await getClasses();

  const filteredData = data.filter((data) => data.classId == classId);

  return filteredData[0];
}

export async function newClass(classData: Class): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {Class} classRepData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (classData.classId != null) form.append("classId", classData.classId);
  if (classData.classRep != null) form.append("classRep", classData.classRep);

  const response = await fetch(`${API_URL}/v1/classes`, {
    method: "POST",
    body: form,
  });

  if (response.status != 201) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function updateClass(
  classId: string,
  classData: Partial<Class>
): Promise<boolean> {
  /**
   * @export
   * @param {string} classId
   * @param {Partial<Class>} classData
   * @return {*} {Promise<boolean>}
   */
  const form = new FormData();

  if (classData.classRep != null) form.append("classRep", classData.classRep);

  const response = await fetch(`${API_URL}/v1/classes?classId=${classId}`, {
    method: "PUT",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteClass(classId: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} classId
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/classes?classId=${classId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
