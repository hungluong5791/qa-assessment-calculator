import { CustomScreenshotWriter } from 'gauge-ts';
import { join, basename } from 'path';

import { screenshot } from 'taiko';

/**
 * Custom class to wire Gauge screenshot function to Taiko screenshot API
 */
export default class ScreenshotWriter {

    @CustomScreenshotWriter()
    public async screenshot(): Promise<string> {
        const screenshotFilePath = join(
            process.env['gauge_screenshots_dir'],
            `screenshot-${process.hrtime.bigint()}.png`,
        );

        await screenshot({ path: screenshotFilePath });
        return basename(screenshotFilePath);
    }
}