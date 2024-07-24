import { API_URL, User } from "src/types";

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
