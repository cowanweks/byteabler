import { API_URL, User, Response } from "../types";

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

export async function signIn(
  username: string,
  password: string
): Promise<Response> {
  /**
   *
   *
   */

  const form = new FormData();

  if (username != null) form.append("username", username);
  if (password != null) form.append("password", password);

  const response = await fetch(`${API_URL}/v1/signin`, {
    method: "POST",
    body: form,
  });

  const responseData = await response.json();

  if (response.status == 400 || response.status == 500) {
    throw new Error("HTTPERROR: " + responseData);
  }

  return {
    status: response.status,
    msg: responseData,
  };
}
