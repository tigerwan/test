#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
import argparse
import os
import logging
import sys
import json

logging.getLogger().setLevel(logging.DEBUG)

# read terraform plan output file in a list
def write_email(path, content):
    with open(path, 'w') as fd:
        fd.write(content)


# read file by lines
def read_lines(path):
    with open(path, 'r') as fd:
        content = fd.readlines()
    return content


# read file as a whole
def read_json(path):
    with open(path, 'r') as fd:
        content = json.load(fd)
    return content

"""
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
"""

# parse arguments
def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', nargs='?', default='templates/email_template.jinja', help='path of jinja format email body template, default is templates/email_template.jinja')
    parser.add_argument('-p', nargs='?', default='plan.text', help='path of terraform plan output file, default is plan.text')
    parser.add_argument('-v', nargs='?', default='variables.json', help='path of the variable file(JSON), default is variables.json')
    parser.add_argument('-o', nargs='?', default='email.html', help='path of email html body, default is email.html')

    args = parser.parse_args()

    return args


def render_template(template_path, template_file, render_data):
    # load jinja template
    env = Environment(
        loader=FileSystemLoader(template_path),
        cache_size=0
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

    # get current working directory
    cwd = os.getcwd()

    # get files path
    email_template_path = os.path.join(cwd, args.t)
    email_template_dir = os.path.dirname(email_template_path) or './'
    email_template_file = os.path.basename(email_template_path)
    terraform_plan_output_path = os.path.join(cwd, args.p)
    variables_path = os.path.join(cwd, args.v)
    output_path = os.path.join(cwd, args.o)

    # validate the file path
    if not os.path.isfile(email_template_path):
        logging.error('Error: template file "{}" does not exist'.format(email_template_path))
        sys.exit(1)

    if not os.path.isfile(terraform_plan_output_path):
        logging.error('Error: terraform plan output file "{}" does not exist'.format(terraform_plan_output_path))
        sys.exit(1)

    # init rendering data
    render_data = {}

    # read terraform plan output plain text file
    logging.info('Load terraform plan text file "{}"'.format(email_template_path))
    raw_plan_output = read_lines(terraform_plan_output_path)
    render_data["terrafrom_plan_output"] = raw_plan_output

    # read variables if the file exists
    if os.path.isfile(variables_path):
        logging.info('Load variables file "{}"'.format(variables_path))
        variables = read_json(variables_path)
        if variables:
            render_data.update(variables)

    # render
    logging.info('Render the template file')
    html_email = render_template(email_template_dir, email_template_file, render_data)

    # write the html format email body to a file
    logging.info('Generate email body to file "{}"'.format(output_path))
    write_email(output_path, html_email)

    logging.info('Email is generated ...')
    sys.exit(0)
