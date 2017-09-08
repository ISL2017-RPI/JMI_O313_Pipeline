import sys
import JMI_O313
import numpy as np

def JMI(data_file, target_file, hm_feat):
    my_JMI = JMI_O313.initialize()
    feat = my_JMI.JMI_primitive_O313(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    hm_feat = 50
    selected_feature = np.array(JMI(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O313_JMI.csv', selected_feature, delimiter=',')
    print selected_feature