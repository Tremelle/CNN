
# Code snippet for saving/loading model weights.

   def save(self,file):
        # save model weights to file
        with open(file,'w') as f:
            f.write('weights_IH\n')
            for j in range(model.N_hidden):
                f.write('{0}\n'.format(','.join(map(str,model.weights_IH[j]))))
            f.write('biases_IH\n')
            f.write('{0}\n'.format(','.join(map(str,model.biases_IH))))
            f.write('weights_HO\n')
            for k in range(model.N_output):
                f.write('{0}\n'.format(','.join(map(str,model.weights_HO[k]))))
            f.write('biases_HO\n')
            f.write('{0}\n'.format(','.join(map(str,model.biases_HO))))
        print("Model saved to {0}.".format(file))

    def load(self,file):
        # load saved model weights
        
        with open(file,'r') as f:
            datareader = csv.reader(f)

            # read weights_IH and biases_IH	
            header = next_datareader(datareader)
            row_count = 0
            for row in datareader:
                if row_count >= self.N_hidden:
                    bias_row = next_datareader(datareader)
                    for i in range(len(bias_row)):
                        self.biases_IH[i] = float(bias_row[i])
                    break
                for i in range(len(row)):
                    self.weights_IH[row_count][i] = float(row[i])
                row_count += 1

            # read weights_HO and biases_HO
            header = next_datareader(datareader)
            row_count = 0
            for row in datareader:
                if row_count >= self.N_output:
                    bias_row = next_datareader(datareader)
                    for i in range(len(bias_row)):
                        self.biases_HO[i] = float(bias_row[i])
                    break
                for i in range(len(row)):
                    self.weights_HO[row_count][i] = float(row[i])
                row_count += 1
        print("Loaded model weights from file: {0}".format(file))
