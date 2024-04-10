import { BASE_URL } from '../';
import { test, expect } from '@playwright/test';
import { mockIPC, mockWindows } from '@tauri-apps/api/mocks';


test('Get classes', async ({page}) => {
    await page.goto(BASE_URL)


})