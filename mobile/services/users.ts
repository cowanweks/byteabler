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

export async function signIn(username: string, password: string): Promise<boolean> {
  /**
   *
   *
   */

  const form = new FormData();

  if (username != null) form.append("username", username);
  if (password != null) form.append("password", password);

  const response = await fetch(`${API_URL}/signin`,
    { method: "POST",
      body: form
     });

  const responsedata = await response.json();

  if (!response.ok) {
    throw new Error("HTTPERROR: " + responsedata);
  }


  return responsedata;
}