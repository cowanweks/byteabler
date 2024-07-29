import { API_URL, Unit, Response } from "../types";

export async function getUnits(): Promise<Array<Unit>> {
  /**
   *
   */
  const response = await fetch(`${API_URL}/v1/units`, { method: "GET" });

  if (response.status != 200) {
    throw Error("HTTP ERROR: " + response.body);
  }

  const data: Array<Unit> = await response.json();

  return data;
}

export async function getUnitByCode(unitCode: string): Promise<Unit> {
  /**
   *
   *
   * @export
   * @return {*}  {Promise<Unit>}
   */
  const units: Array<Unit> = await getUnits();

  const filteredUnit = units.filter((unit) => unit.unitCode == unitCode);

  return filteredUnit[0];
}

export async function newUnit(unitData: Unit): Promise<Response> {
  /**
   *
   *
   * @export
   * @param {Unit} uniData
   * @return {*}  {Promise<boolean>}
   */

  const form = new FormData();

  if (unitData.unitCode != null) form.append("unitCode", unitData.unitCode);
  if (unitData.unitName != null) form.append("unitName", unitData.unitName);

  const response = await fetch(`${API_URL}/v1/units`, {
    method: "POST",
    body: form,
  });

  const responseData = await response.json();

  if (response.status == 400 || response.status == 500) {
    throw new Error(`HTTP ERROR: ${responseData}`);
  }

  return {status: response.status, msg: responseData};
}

export async function updateUnit(
  unitCode: string,
  unitData: Partial<Unit>
): Promise<boolean> {
  /**
   * @export
   * @param {string} unitCode
   * @param {Partial<Unit>} unitData
   * @return {*} {Propise<boolean>}
   */
  const form = new FormData();

  if (unitData.unitCode != null) form.append("unitCode", unitData.unitCode);
  if (unitData.unitName != null) form.append("unitName", unitData.unitName);

  const response = await fetch(`${API_URL}/v1/units?unitCode=${unitCode}`, {
    method: "PUT",
    body: form,
  });

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}

export async function deleteUnit(unitCode: string): Promise<boolean> {
  /**
   *
   *
   * @export
   * @param {string} unitCode
   * @return {*}  {Promise<boolean>}
   */

  const response = await fetch(`${API_URL}/v1/units?unitCode=${unitCode}`);

  if (!response.ok) {
    throw Error("HTTP ERROR: " + response.body);
  }

  return true;
}
