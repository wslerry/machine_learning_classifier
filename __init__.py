# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MachineLearningClassifier
                                 A QGIS plugin
 Satellite image classification based on machine learning
                             -------------------
        begin                : 2018-12-11
        copyright            : (C) 2018 by lerryws
        email                : @wslerry2@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MachineLearningClassifier class from file MachineLearningClassifier.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .machine_learning_classifier import MachineLearningClassifier
    return MachineLearningClassifier(iface)
