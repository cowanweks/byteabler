import { API_URL, User } from "../types";

export async function getUsers(): Promise<Array<User>> {
  /**
   *
   *
   */
  const response = await fetch(`${API_URL}/users`, { method: "GET" });

  if (!response.ok) {
    throw new Error("HTTPERROR: " + response.body);
  }

  const responsedata: Array<User> = await response.json();

  return responsedata;
}

export async function signIn(
  userData: Omit<User, "userId" | "roles">
): Promise<boolean> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (userData.username) form.append("username", userData.username);
  if (userData.password) form.append("password", userData.password);

  const response = await fetch(`${API_URL}/signin`, {
    method: "POST",
    body: form,
  });

  if (response.ok) {
    return true;
  }

  return false;
}

export async function signOut(): Promise<boolean> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<boolean>}
   */
  const response = await fetch(`${API_URL}/signout`, { method: "GET" });

  if (!response.ok) {
    throw new Error("HTTPERROR: " + response.body);
  }

  return true;
}
