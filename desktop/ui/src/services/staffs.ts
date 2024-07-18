import { API_URL, Staff } from "@types/index";

export async function getStaffs(): Promise<Array<Staff>> {
  /**
   *
   */
  const response = await fetch(`${API_URL}/v1/staffs`, { method: "GET" });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<Staff> = await response.json();

  console.log(data)

  return data;
}

export async function getStaffByCode(staffNo: string): Promise<Staff> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<Staff>}
   */
  const staffs: Array<Staff> = await getStaffs();

  const filteredStaff = staffs.filter((staff) => staff.staffNo == staffNo);

  return filteredStaff[0];
}

export async function newStaff(staffData: Staff): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {Staff} staffData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (staffData.firstName != null) form.append("unitCode", staffData.firstName);
  if (staffData.middleName != null) form.append("unitName", staffData.middleName);

  const response = await fetch(`${API_URL}/v1/staffs`, {
    method: "POST",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function updateStaff(
  staffNo: string,
  staffData: Partial<Staff>
): Promise<boolean> {
  /**
   * @export
   * @param {string} staffNo
   * @param {Partial<Staff>} staffData
   * @return {*} {Promise<boolean>}
   */
  const form = new FormData();

  if (staffData.firstName != null) form.append("unitCode", staffData.firstName);
  if (staffData.middleName != null) form.append("unitName", staffData.middleName);

  const response = await fetch(`${API_URL}/v1/staffs/${staffNo}`, {
    method: "PUT",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteStaff(staffNo: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} staffNo
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/staffs/${staffNo}`);

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
