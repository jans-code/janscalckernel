#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""calc kernel install helper"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

JSON = """{"argv":["python","-m","janscalckernel", "-f",
"{connection_file}"], "display_name":"calc"}"""

SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   id="svg11300"
   height="300"
   width="300"
   version="1.1"
   sodipodi:docname="calc.svg"
   inkscape:export-filename="logo-svg.svg"
   inkscape:export-xdpi="96"
   inkscape:export-ydpi="96"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/">
  <sodipodi:namedview
     id="namedview34"
     pagecolor="#505050"
     bordercolor="#ffffff"
     borderopacity="1"
     inkscape:showpageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="1"
     inkscape:deskcolor="#505050"
     showgrid="false" />
  <defs
     id="defs3">
    <radialGradient
       id="radialGradient6719"
       cx="605.71002"
       xlink:href="#linearGradient5060"
       gradientUnits="userSpaceOnUse"
       cy="486.64999"
       r="117.14"
       gradientTransform="matrix(-2.7744,0,0,1.9697,112.76,-872.89)" />
    <linearGradient
       id="linearGradient5060">
      <stop
         id="stop5062"
         offset="0" />
      <stop
         id="stop5064"
         stop-opacity="0"
         offset="1" />
    </linearGradient>
    <radialGradient
       id="radialGradient6717"
       cx="605.71002"
       xlink:href="#linearGradient5060"
       gradientUnits="userSpaceOnUse"
       cy="486.64999"
       r="117.14"
       gradientTransform="matrix(2.7744,0,0,1.9697,-1891.6,-872.89)" />
    <linearGradient
       id="linearGradient6715"
       y2="609.51001"
       gradientUnits="userSpaceOnUse"
       y1="366.64999"
       gradientTransform="matrix(2.7744,0,0,1.9697,-1892.2,-872.89)"
       x2="302.85999"
       x1="302.85999">
      <stop
         id="stop5050"
         stop-opacity="0"
         offset="0" />
      <stop
         id="stop5056"
         offset=".5" />
      <stop
         id="stop5052"
         stop-opacity="0"
         offset="1" />
    </linearGradient>
    <radialGradient
       id="radialGradient2939"
       cx="25.458"
       gradientUnits="userSpaceOnUse"
       cy="35.596001"
       r="20.531"
       gradientTransform="matrix(2.1282,0,0,2.1283,-28.519,-40.418)">
      <stop
         id="stop2935"
         stop-color="#9cbcde"
         offset="0" />
      <stop
         id="stop2937"
         stop-color="#204a87"
         offset="1" />
    </radialGradient>
  </defs>
  <metadata
     id="metadata4">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:creator>
          <cc:Agent>
            <dc:title>Jakub Steiner</dc:title>
          </cc:Agent>
        </dc:creator>
        <dc:source>http://jimmac.musichall.cz</dc:source>
        <cc:license
           rdf:resource="http://creativecommons.org/licenses/by-sa/2.0/" />
        <dc:title>Accessibility</dc:title>
        <dc:subject>
          <rdf:Bag>
            <rdf:li>accessibility</rdf:li>
            <rdf:li>assist</rdf:li>
          </rdf:Bag>
        </dc:subject>
      </cc:Work>
      <cc:License
         rdf:about="http://creativecommons.org/licenses/by-sa/2.0/">
        <cc:permits
           rdf:resource="http://web.resource.org/cc/Reproduction" />
        <cc:permits
           rdf:resource="http://web.resource.org/cc/Distribution" />
        <cc:requires
           rdf:resource="http://web.resource.org/cc/Notice" />
        <cc:requires
           rdf:resource="http://web.resource.org/cc/Attribution" />
        <cc:permits
           rdf:resource="http://web.resource.org/cc/DerivativeWorks" />
        <cc:requires
           rdf:resource="http://web.resource.org/cc/ShareAlike" />
      </cc:License>
    </rdf:RDF>
  </metadata>
  <g
     id="layer1"
     transform="matrix(6.3997189,0,0,6.3997189,-12.503676,-9.5361519)">
    <g
       id="g6707"
       transform="matrix(0.02299,0,0,0.023454,45.841,39.649)">
      <rect
         id="rect6709"
         opacity="0.40206"
         style="color:#000000;fill:url(#linearGradient6715)"
         height="478.35999"
         width="1339.6"
         y="-150.7"
         x="-1559.3"
         fill="url(#linearGradient6715)" />
      <path
         id="path6711"
         opacity="0.40206"
         style="color:#000000;fill:url(#radialGradient6717)"
         d="m -219.62,-150.68 v 478.33 c 142.88,0.9 345.4,-107.17 345.4,-239.2 0,-132.02 -159.44,-239.13 -345.4,-239.13 z"
         fill="url(#radialGradient6717)" />
      <path
         id="path6713"
         opacity="0.40206"
         style="color:#000000;fill:url(#radialGradient6719)"
         d="m -1559.3,-150.68 v 478.33 c -142.8,0.9 -345.4,-107.17 -345.4,-239.2 0,-132.02 159.5,-239.13 345.4,-239.13 z"
         fill="url(#radialGradient6719)" />
    </g>
    <rect
       id="rect11518"
       stroke-linejoin="bevel"
       height="40.062"
       stroke="#3465a4"
       fill="url(#radialGradient2939)"
       style="color:#000000;fill:url(#radialGradient2939)"
       fill-rule="evenodd"
       rx="5.4548001"
       ry="5.4548001"
       width="40.062"
       stroke-miterlimit="10"
       y="3.0232999"
       x="4.9147" />
    <rect
       id="rect11528"
       stroke-linejoin="bevel"
       height="37.101002"
       stroke="#ffffff"
       stroke-width="2"
       fill="none"
       style="color:#000000"
       rx="3.9068"
       ry="3.9068"
       width="37.101002"
       stroke-miterlimit="10"
       y="4.5040002"
       x="6.3954" />
    <path
       id="path9990"
       d="m 12.5,36 c 3,-8 8.155,-12.981 10.5,-13 3.431,-0.028 5,6 9,6 3.606,0 7,-11 8,-19"
       stroke="#ff0000"
       stroke-width="1px"
       fill="none" />
    <path
       id="path9988"
       d="M 12,10 V 36 H 38"
       stroke="#ffffff"
       stroke-width="2"
       fill="none" />
    <path
       id="path9992"
       fill="#ffffff"
       d="m 12,7 -3,6 h 6 L 12,7"
       fill-rule="evenodd" />
    <path
       id="path9994"
       fill="#ffffff"
       d="m 41,36 -6,-3 v 6 l 6,-3"
       fill-rule="evenodd" />
    <g
       id="g10167"
       transform="matrix(3.5134,0,0,3.5134,-53.717,-11.668)"
       stroke="#ffffff"
       stroke-width="0.14231"
       fill="#ffffff">
      <g
         id="g10169"
         xml:space="preserve"
         fill-rule="evenodd"
         transform="matrix(0.068571,0,0,-0.068571,-12,36)"
         stroke="#ffffff"
         stroke-miterlimit="10.433"
         stroke-width="2.0754"
         fill="#ffffff"><path
           id="path10171"
           d="m 474.28,425.93 h 4.29 c 0.99,0 1.49,0 1.49,0.99 0,0.55 -0.5,0.55 -1.35,0.55 h -4.13 c 0.55,2.89 0.5,2.79 1.05,5.68 0.19,1.05 0.89,4.58 1.19,5.18 0.45,0.94 1.3,1.69 2.34,1.69 0.2,0 1.5,0 2.45,-0.89 -2.2,-0.2 -2.7,-1.95 -2.7,-2.69 0,-1.15 0.9,-1.75 1.85,-1.75 1.29,0 2.74,1.1 2.74,2.99 0,2.29 -2.29,3.44 -4.34,3.44 -1.69,0 -4.83,-0.9 -6.32,-5.83 -0.3,-1.05 -0.45,-1.54 -1.65,-7.82 h -3.43 c -0.95,0 -1.5,0 -1.5,-0.95 0,-0.59 0.45,-0.59 1.4,-0.59 h 3.29 l -3.74,-19.68 c -0.9,-4.83 -1.75,-9.37 -4.33,-9.37 -0.2,0 -1.45,0 -2.4,0.9 2.29,0.15 2.74,1.94 2.74,2.69 0,1.15 -0.89,1.74 -1.84,1.74 -1.29,0 -2.74,-1.09 -2.74,-2.98 0,-2.25 2.19,-3.44 4.24,-3.44 2.73,0 4.73,2.94 5.62,4.83 1.6,3.14 2.74,9.17 2.79,9.51 z" /><path
           id="path10173"
           d="m 501.49,394.04 v 0.03 0.03 l -0.01,0.01 v 0.02 0.01 l -0.01,0.02 v 0.02 l -0.01,0.01 -0.01,0.02 -0.01,0.02 -0.01,0.03 -0.01,0.02 -0.02,0.02 -0.02,0.03 -0.02,0.03 -0.02,0.03 -0.03,0.03 -0.03,0.04 -0.01,0.02 -0.02,0.02 -0.02,0.02 -0.02,0.02 -0.02,0.02 -0.02,0.03 -0.02,0.02 -0.02,0.02 -0.02,0.03 -0.03,0.02 -0.02,0.03 -0.03,0.03 -0.02,0.03 -0.03,0.03 -0.03,0.03 -0.03,0.03 -0.03,0.03 -0.03,0.03 -0.04,0.04 -0.03,0.03 -0.04,0.04 -0.03,0.03 -0.04,0.04 -0.04,0.04 c -6.23,6.28 -7.82,15.69 -7.82,23.31 0,8.67 1.89,17.34 8.02,23.57 0.65,0.59 0.65,0.69 0.65,0.84 0,0.35 -0.2,0.5 -0.5,0.5 -0.5,0 -4.98,-3.39 -7.92,-9.72 -2.54,-5.47 -3.14,-11 -3.14,-15.19 0,-3.88 0.55,-9.91 3.29,-15.54 2.99,-6.12 7.27,-9.36 7.77,-9.36 0.3,0 0.5,0.15 0.5,0.49 z" /><path
           id="path10175"
           d="m 521.64,421.04 0.03,0.13 0.03,0.15 0.05,0.17 0.04,0.18 0.06,0.19 0.06,0.21 0.06,0.21 0.07,0.23 0.08,0.23 0.09,0.24 0.1,0.25 0.1,0.24 0.11,0.25 0.12,0.25 0.13,0.25 0.14,0.25 0.15,0.24 0.15,0.24 0.17,0.23 0.18,0.22 0.18,0.22 0.2,0.2 0.21,0.19 0.22,0.18 0.23,0.16 0.25,0.14 0.12,0.07 0.13,0.06 0.13,0.05 0.14,0.05 0.14,0.05 0.14,0.04 0.14,0.03 0.15,0.03 0.15,0.02 0.16,0.02 0.16,0.01 h 0.16 c 0.25,0 1.45,0 2.49,-0.65 -1.4,-0.25 -2.39,-1.49 -2.39,-2.68 0,-0.8 0.55,-1.75 1.89,-1.75 1.1,0 2.69,0.9 2.69,2.89 0,2.59 -2.94,3.29 -4.63,3.29 -2.89,0 -4.64,-2.64 -5.23,-3.79 -1.24,3.29 -3.94,3.79 -5.38,3.79 -5.18,0 -8.02,-6.43 -8.02,-7.67 0,-0.5 0.5,-0.5 0.6,-0.5 0.39,0 0.54,0.1 0.64,0.54 1.7,5.29 4.99,6.53 6.68,6.53 0.94,0 2.69,-0.45 2.69,-3.33 0,-1.55 -0.85,-4.89 -2.69,-11.86 -0.8,-3.09 -2.54,-5.18 -4.73,-5.18 -0.3,0 -1.45,0 -2.49,0.65 1.24,0.25 2.34,1.29 2.34,2.69 0,1.34 -1.1,1.74 -1.85,1.74 -1.49,0 -2.73,-1.3 -2.73,-2.89 0,-2.29 2.48,-3.29 4.68,-3.29 3.28,0 5.08,3.49 5.22,3.79 0.61,-1.85 2.4,-3.79 5.39,-3.79 5.13,0 7.97,6.43 7.97,7.68 0,0.49 -0.45,0.49 -0.6,0.49 -0.45,0 -0.55,-0.2 -0.65,-0.55 -1.64,-5.33 -5.03,-6.52 -6.62,-6.52 -1.94,0 -2.74,1.59 -2.74,3.29 0,1.09 0.3,2.19 0.85,4.38 z" /><path
           id="path10177"
           d="m 547.4,418.45 -0.01,0.37 v 0.39 l -0.01,0.39 -0.01,0.41 -0.04,0.84 -0.06,0.88 -0.09,0.92 -0.1,0.94 -0.14,0.98 -0.16,1 -0.2,1.02 -0.23,1.04 -0.27,1.05 -0.3,1.06 -0.35,1.06 -0.39,1.07 -0.22,0.53 -0.22,0.54 -0.24,0.53 -0.25,0.53 c -2.99,6.12 -7.27,9.36 -7.77,9.36 -0.3,0 -0.5,-0.2 -0.5,-0.5 0,-0.15 0,-0.25 0.94,-1.15 4.89,-4.92 7.73,-12.85 7.73,-23.26 0,-8.52 -1.85,-17.28 -8.02,-23.56 -0.65,-0.6 -0.65,-0.69 -0.65,-0.85 0,-0.29 0.2,-0.49 0.5,-0.49 0.5,0 4.98,3.38 7.92,9.71 2.54,5.48 3.14,11.01 3.14,15.19 z" /></g>
    </g>
  </g>
</svg>"""


def install_kernelspec():
    """create dir + file and install kernel"""
    kerneldir = "/tmp/janscalckernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w", encoding="UTF-8") as file:
        file.write(JSON)

    with open(kerneldir + "logo-svg.svg", "w", encoding="UTF-8") as file:
        file.write(SVG)

    print(' Done!')
    print('Installing Jupyter kernel...', end="")

    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janscalckernel', user=os.getenv('USER'))

    print(' Done!')
    print('Cleaning up tmp files...', end="")

    shutil.rmtree(kerneldir)

    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janscalckernel')
    