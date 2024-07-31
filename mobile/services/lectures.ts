import { API_URL, Lecture, Response } from "@/types";

export async function getLectures(): Promise<Array<Lecture>> {
  /**
   *
   */
  const response = await fetch(`${API_URL}/v1/lectures`, { method: "GET" });

  if (response.status != 200) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<Lecture> = await response.json();

  return data;
}

export async function getLectureByCode(lectureId: string): Promise<Lecture> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<Lecture>}
   */
  const lectures: Array<Lecture> = await getLectures();

  const filteredLecture = lectures.filter(
    (lecture) => lecture.lectureId == lectureId
  );

  return filteredLecture[0];
}

export async function newLecture(lectureData: Lecture): Promise<Response> {
  /**
   *
   *
   * @export
   * @param {Lecture} uniData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  console.log(lectureData);

  if (lectureData.classId != null) form.append("classId", lectureData.classId);
  if (lectureData.unitCode != null)
    form.append("unitCode", lectureData.unitCode);
  if (lectureData.lecturer != null)
    form.append("lecturer", lectureData.lecturer);
  if (lectureData.weekDay != null) form.append("weekDay", lectureData.weekDay);
  if (lectureData.time != null) form.append("time", lectureData.time);

  const response = await fetch(`${API_URL}/v1/lectures`, {
    method: "POST",
    body: form,
  });

  const responseData = await response.json();

  console.log(responseData);

  if (response.status == 500) {
    throw new Error(`HTTP ERROR: ${responseData}`);
  }

  return { status: response.status, msg: responseData };
}

export async function updateLecture(
  lectureId: string,
  lectureData: Partial<Lecture>
): Promise<boolean> {
  /**
   * @export
   * @param {string} lectureId
   * @param {Partial<Lecture>} lectureData
   * @return {*} {Promise<boolean>}
   */
  const form = new FormData();

  if (lectureData.classId != null) form.append("classId", lectureData.classId);
  if (lectureData.unitCode != null)
    form.append("unitCode", lectureData.unitCode);
  if (lectureData.lecturer != null)
    form.append("lecturer", lectureData.lecturer);
  if (lectureData.weekDay != null) form.append("weekDay", lectureData.weekDay);
  if (lectureData.time != null) form.append("time", lectureData.time);

  const response = await fetch(
    `${API_URL}/v1/lectures?lectureId=${lectureId}`,
    {
      method: "PUT",
      body: form,
    }
  );

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteLecture(lectureId: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} lectureId
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/lectures?lectureId=${lectureId}`);

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
