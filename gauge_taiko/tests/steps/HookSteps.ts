import { AfterStep, AfterSuite, BeforeSuite, ExecutionContext, Gauge } from "gauge-ts";
import { closeBrowser, openBrowser, screenshot } from "taiko";
// @ts-ignore: Plugin
import path = require("path");
import yn = require("yn");

export default class HookSteps {
    @BeforeSuite()
    public async beforeSuite() {
        await openBrowser({
            headless: yn(process.env.HEADLESS, {
                default: false,
            })
        });
    }

    @AfterSuite()
    public async afterSuite() {
        await closeBrowser();
    };
}