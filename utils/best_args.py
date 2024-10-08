# Copyright 2022-present, Lorenzo Bonicelli, Pietro Buzzega, Matteo Boschini, Angelo Porrello, Simone Calderara.
# All rights reserved.
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""
This module contains the best hyperparameters on a small selection of datasets and models.

The hyperparameters are organized in a dictionary with the following structure:
      {
            'dataset_name': {
                  'model_name': {
                        'buffer_size': {
                              'hyperparameter_name': hyperparameter_value
                        }
                  }
            }
      }

Todolist:
      * Add more hyperparameters
      * Add more datasets
      * Add more models
"""

best_args = {
    'seq-cifar10': {'sgd': {-1: {'lr': 0.1,
                                 'batch_size': 32,
                                 'n_epochs': 50}},
                    'ewc_on': {-1: {'lr': 0.03,
                                    'e_lambda': 10,
                                    'gamma': 1.0,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'si': {-1: {'lr': 0.03,
                                'c': 0.5,
                                'xi': 1.0,
                                'batch_size': 32,
                                'n_epochs': 50}},
                    'lwf': {-1: {'lr': 0.01,
                                 'alpha': 3.0,
                                 'softmax_temp': 2.0,
                                 'batch_size': 32,
                                 'n_epochs': 50,
                                 'optim_wd': 0.0005}},
                    'pnn': {-1: {'lr': 0.03, 'batch_size': 32,
                                 'n_epochs': 50}},
                    'er': {50: {'lr': 0.1,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 50},
                           125: {'lr': 0.1,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 50}},
                    'gem': {50: {'lr': 0.03,
                                  'gamma': 0.5,
                                  'batch_size': 32,
                                  'n_epochs': 50},
                            125: {'lr': 0.03, 'gamma': 0.5,
                                  'batch_size': 32,
                                  'n_epochs': 50}},
                    'agem': {50: {'lr': 0.03,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 50},
                             125: {'lr': 0.03,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 50}},
                    'hal': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'batch_size': 32,
                                  'n_epochs': 50,
                                  'hal_lambda': 0.2,
                                  'beta': 0.5,
                                  'gamma': 0.1,
                                  'steps_on_anchors': 100,
                                  'finetuning_epochs': 1},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'batch_size': 32,
                                  'n_epochs': 50,
                                  'hal_lambda': 0.1,
                                  'beta': 0.3,
                                  'gamma': 0.1,
                                  'steps_on_anchors': 100,
                                  'finetuning_epochs': 1}},
                    'gss': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'gss_minibatch_size': 32,
                                  'batch_size': 32,
                                  'n_epochs': 50,
                                  'batch_num': 1},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'gss_minibatch_size': 32,
                                  'batch_size': 32,
                                  'n_epochs': 50,
                                  'batch_num': 1}},
                    'agem_r': {50: {'lr': 0.03,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 50},
                               125: {'lr': 0.03,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 50}},
                    'icarl': {50: {'lr': 0.1,
                                    'minibatch_size': 0,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 50},
                              125: {'lr': 0.1,
                                    'minibatch_size': 0,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'fdr': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.3,
                                  'batch_size': 32,
                                  'n_epochs': 50},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 1,
                                  'batch_size': 32,
                                  'n_epochs': 50}},
                    'der': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.3,
                                  'batch_size': 32,
                                  'n_epochs': 50},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.3,
                                  'batch_size': 32,
                                  'n_epochs': 50}},
                    'derpp': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 50},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.2,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'er-ace': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'clser': {
                        50: {
                            'reg_weight': 0.15,
                            'stable_model_update_freq': 0.1,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.5,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        },
                        125: {
                            'reg_weight': 0.15,
                            'stable_model_update_freq': 0.2,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.9,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        }},
                  },
    'seq-tinyimg': {'sgd': {-1: {'lr': 0.03,
                                 'batch_size': 32,
                                 'n_epochs': 100}},
                    'ewc_on': {-1: {'lr': 0.03,
                                    'e_lambda': 25,
                                    'gamma': 1.0,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'si': {-1: {'lr': 0.03,
                                'c': 0.5,
                                'xi': 1.0,
                                'batch_size': 32,
                                'n_epochs': 100}},
                    'lwf': {-1: {'lr': 0.01,
                                 'alpha': 1.0,
                                 'softmax_temp': 2.0,
                                 'batch_size': 32,
                                 'n_epochs': 100,
                                 'optim_wd': 0.0005}},
                    'pnn': {-1: {'lr': 0.03, 'batch_size': 32,
                                 'n_epochs': 100}},
                    'er': {50: {'lr': 0.1,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 100},
                           125: {'lr': 0.03,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 100}},
                    'agem': {50: {'lr': 0.01,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 100},
                             125: {'lr': 0.01,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 100}},
                    'agem_r': {50: {'lr': 0.01,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 100},
                               125: {'lr': 0.01,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 100}},
                    'icarl': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 100},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'fdr': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.3,
                                  'batch_size': 32,
                                  'n_epochs': 100},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 1,
                                  'batch_size': 32,
                                  'n_epochs': 100}},
                    'der': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'softmax_temp': 2.0,
                                  'alpha': 0.1,
                                  'batch_size': 32,
                                  'n_epochs': 100},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.1,
                                  'batch_size': 32,
                                  'n_epochs': 100}},
                    'derpp': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 100},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'er-ace': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'clser': {
                        50: {
                            'reg_weight': 0.1,
                            'stable_model_update_freq': 0.08,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.16,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        },
                        125: {
                            'reg_weight': 0.1,
                            'stable_model_update_freq': 0.1,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.16,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        }},
                  },
    'seq-imagenet-r': {'sgd': {-1: {'lr': 0.03,
                                 'batch_size': 32,
                                 'n_epochs': 100}},
                    'ewc_on': {-1: {'lr': 0.03,
                                    'e_lambda': 25,
                                    'gamma': 1.0,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'si': {-1: {'lr': 0.03,
                                'c': 0.5,
                                'xi': 1.0,
                                'batch_size': 32,
                                'n_epochs': 100}},
                    'lwf': {-1: {'lr': 0.01,
                                 'alpha': 1.0,
                                 'softmax_temp': 2.0,
                                 'batch_size': 32,
                                 'n_epochs': 100,
                                 'optim_wd': 0.0005}},
                    'pnn': {-1: {'lr': 0.03, 'batch_size': 32,
                                 'n_epochs': 100}},
                    'er': {50: {'lr': 0.1,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 100},
                           125: {'lr': 0.03,
                                 'minibatch_size': 32,
                                 'batch_size': 32,
                                 'n_epochs': 100}},
                    'agem': {50: {'lr': 0.01,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 100},
                             125: {'lr': 0.01,
                                   'minibatch_size': 32,
                                   'batch_size': 32,
                                   'n_epochs': 100}},
                    'agem_r': {50: {'lr': 0.01,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 100},
                               125: {'lr': 0.01,
                                     'minibatch_size': 32,
                                     'batch_size': 32,
                                     'n_epochs': 100}},
                    'icarl': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 100},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'softmax_temp': 2.0,
                                    'optim_wd': 0.00001,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'fdr': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.3,
                                  'batch_size': 32,
                                  'n_epochs': 100},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 1,
                                  'batch_size': 32,
                                  'n_epochs': 100}},
                    'der': {50: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'softmax_temp': 2.0,
                                  'alpha': 0.1,
                                  'batch_size': 32,
                                  'n_epochs': 100},
                            125: {'lr': 0.03,
                                  'minibatch_size': 32,
                                  'alpha': 0.1,
                                  'batch_size': 32,
                                  'n_epochs': 100}},
                    'derpp': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 100},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'n_epochs': 100}},
                    'er-ace': {50: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50},
                              125: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'batch_size': 32,
                                    'n_epochs': 50}},
                    'clser': {
                        50: {
                            'reg_weight': 0.1,
                            'stable_model_update_freq': 0.08,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.16,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        },
                        125: {
                            'reg_weight': 0.1,
                            'stable_model_update_freq': 0.1,
                            'stable_model_alpha': 0.999,
                            'plastic_model_update_freq': 0.16,
                            'plastic_model_alpha': 0.999,
                            'lr': 0.1,
                            'minibatch_size': 32,
                            'batch_size': 32,
                            'n_epochs': 50,
                        }},

                    }
}
