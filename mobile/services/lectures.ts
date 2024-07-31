import { API_URL, Lecture, Response } from "@/types";

export async function getLectures(options: {
  user: string;
  role: string;
  day: string | undefined;
}): Promise<Array<Lecture>> {
  /**
   *
   */

  let template: string = ``;

  if (options.role == "Lecturer") {
    template = template.concat(`?staffNo=${options.user}`);
  }

  if (options.role == "ClassRep") {
    template = template.concat(`?regNo=${options.user}`);
  }

  if (options.day != undefined) {
    template = template.concat(`&day=${options.day}`);
  }

  const response = await fetch(`${API_URL}/v1/lectures${template}`, {
    method: "GET",
  });

  if (response.status != 200) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<Lecture> = await response.json();

  return data;
}

export async function getLectureByCode(
  lectureId: string,
  options: { user: string; role: string; day: string }
): Promise<Lecture> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<Lecture>}
   */
  const lectures: Array<Lecture> = await getLectures(options);

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
