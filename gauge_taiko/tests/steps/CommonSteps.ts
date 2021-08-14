
import { Gauge, Step, Table } from "gauge-ts";

import { checkBox, click, evaluate, goto, into, link, press, screenshot, text, textBox, toLeftOf, write } from 'taiko';

export default class CommonSteps {

    @Step("Open Application at endpoint <endpoint_url>")
    public async openAppEndpointUrl(endpointUrl: string) {
        const baseUrl = process.env.BASE_URL;
        if (endpointUrl.startsWith('/')) {
            endpointUrl = endpointUrl.substring(1);
        }

        await goto(`${baseUrl}/${endpointUrl}`, {
            navigationTimeout: 60000
        });
    }
}
