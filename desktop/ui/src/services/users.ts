import { API_URL, User, Response } from "@/types";

export async function getUsers(): Promise<Array<User>> {
  /**
   *
   *
   */
  const response = await fetch(`${API_URL}/v1/users`, { method: "GET" });

  if (!response.ok) {
    throw new Error("HTTPERROR: " + response.body);
  }

  const responsedata: Array<User> = await response.json();

  return responsedata;
}

export async function getUserById(userName: string): Promise<User> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<User>}
   */
  const data: Array<User> = await getUsers();

  const filteredData = data.filter((data) => data.userName == userName);

  return filteredData[0];
}

export async function newUser(userData: User): Promise<Response> {
  /**
   *
   *
   * @export
   * @param {User} userData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (userData.staffNo != null) form.append("staffNo", userData.staffNo);
  if (userData.userName != null) form.append("userName", userData.userName);
  if (userData.password != null) form.append("password", userData.password);
  if (userData.confirmPassword != null) form.append("confirmPassword",
   userData.confirmPassword);
  if (userData.roles != null) form.append("roles", userData.roles);

  const response = await fetch(`${API_URL}/v1/users`, {
    method: "POST",
    body: form,
  });

  const responseData = await response.json();

  if (response.status == 400 || response.status == 500) {
    console.log(responseData)
    throw new Error(`HTTP ERROR: ${responseData}`);
  }

  return {status: response.status, msg: responseData};
}

export async function updateClass(
  userName: string,
  userData: Partial<User>
): Promise<boolean> {
  /**
   * @export
   * @param {string} classId
   * @param {Partial<User>} classData
   * @return {*} {Promise<boolean>}
   */
  const form = new FormData();

  if (userData.staffNo != null) form.append("staffNo", userData.staffNo);
  if (userData.password != null) form.append("password", userData.password);
  if (userData.roles != null) form.append("roles", userData.roles);

  const response = await fetch(`${API_URL}/v1/users?userName=${userName}`, {
    method: "PUT",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteClass(userName: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} classId
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/users?userName=${userName}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
