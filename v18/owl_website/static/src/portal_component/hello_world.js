import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry"

export class HelloWorld extends Component {
    static template = "owl_website.HelloWorld";
    static props = {};
}

registry.category("public_components").add("owl_website.HelloWorld", HelloWorld);