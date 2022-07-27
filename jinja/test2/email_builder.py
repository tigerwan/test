#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
import argparse
import os
import logging


logging.getLogger().setLevel(logging.DEBUG)

# read terraform plan output file in a list
def write_email(path, content):
    with open(path, 'w') as fd:
        fd.write(content)


# read terraform plan output file in a list
def read_plan_output_file(path):
    content = []
    with open(path, 'r') as fd:
        content = fd.readlines()
    return content


# convert terraform plan output file content to html format and return a list
def plan_output_2_html(content):
    html_content = []
    for line in content:
        html_content.append(line_2_html(line))
    return html_content


# convert a plain text line to html
def line_2_html(line):
    html_line = ''

    # highlight
    if len(line.strip()) <= 0:           # new line
        # html_line = '<br />'
        pass
    elif line.strip().startswith('+'):   # green resource/propery to add
        html_line = '<p style="color:rgb(0, 255, 0);">{}</p>'.format(line)
    elif line.strip().startswith('-'):   # red the resource/propery to remove
        html_line = '<p style="color:rgb(255, 0, 0);">{}</p>'.format(line)
    elif line.strip().startswith('~'):   # yellow the resource/propery to update
        html_line = '<p style="color:rgb(255, 191, 0);">{}</p>'.format(line)
    elif line.strip().startswith('#'):   # bold the resource name
        html_line = '<p><b>{}</b></p>'.format(line)
    else:                               # other lines
        html_line = '<p>{}</p>'.format(line)

    # indentation
    html_line = html_line.replace('  ', '&emsp;')

    return html_line


# parse arguments
def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', nargs='?', default='templates/email_template.jinja', help='path of jinja format email body template, default is templates/email_template.jinja')
    parser.add_argument('-p', nargs='?', default='plan.text', help='path of terraform plan output file, default is plan.text')
    parser.add_argument('-o', nargs='?', default='email.html', help='path of email html body, default is email.html')

    args = parser.parse_args()

    return args


def render_template(template_path, template_file, render_data):
    # load jinja template
    env = Environment(
        loader=FileSystemLoader(template_path)
    )
    template = env.get_template(template_file)

    # render
    output = template.render(**render_data)
    return output


if __name__ == '__main__':

    logging.info('About to generate email ...')
    # parse arguments
    args = parse_arguments()
    logging.debug('CLI arguments:{}'.format(args))

    # get files path
    email_template_dir = os.path.dirname(args.t) or './'
    email_template_file = os.path.basename(args.t)
    terraform_plan_output_path = args.p
    output_path = args.o

    # read terraform plan output plain text file
    raw_plan_output = read_plan_output_file(terraform_plan_output_path)
    logging.info('Loaded terraform plan text file "{}" from "{}" folder'.format(email_template_file, email_template_dir))

    # convert to html format
    html_plan_output = plan_output_2_html(raw_plan_output)
    logging.info('Converted terraform plan file to html format')

    # render
    render_data = {
        "terrafrom_plan_html": '\n'.join(html_plan_output)
    }
    html_email = render_template(email_template_dir, email_template_file, render_data)

    # write the html format email body to a file
    write_email(output_path, html_email)
    logging.info('Write email body to file "{}"'.format(output_path))

    logging.info('Email is generated ...')
