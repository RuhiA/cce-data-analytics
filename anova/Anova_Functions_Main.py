import math

class RegressionModel:
    y_cap_arr = None
    num_estimated_params = None

class AnovaResponse:
    dfe = None
    dfr = None
    sse = None
    ssr = None
    mse = None
    msr = None
    f = None
    p = None
    isSignificant = None

class Anova:
    
    # method to calculate mean of array without using numpy library
    def calc_mean(self, arr):
        sum = 0
        for element in arr:
            sum = sum + element
        mean = sum/len(arr)
        return mean

    
    # method to calculate power of a number without using math library
    def calc_power(self, a, b):
        power = 1;
        for i in range(b):
            power *= a
        return power
    
    
    # computes f-statistics with array arguments
    def compute_anova(self, y_arr, ycap_arr, dfr, alpha_value):
        ybar = self.calc_mean(y_arr)
        
        ssr = self.calculate_ssr(ycap_arr, ybar)
        sse = self.calculate_sse(y_arr, ycap_arr)

        dfe = len(y_arr) - dfr - 1

        msr = self.calculate_msr(ssr, dfr)
        mse = self.calculate_mse(sse, dfe)

        fvalue = self.calculate_f_value(msr, mse)
        
        # computing p-value
        p_value = self.calculate_p_value(dfr, dfe, fvalue)

        # constructing response to be returned
        response = AnovaResponse()
        response.sse = sse
        response.ssr = ssr
        response.mse = mse
        response.msr = msr
        response.f = fvalue
        response.p = p_value
        response.dfe = dfe
        response.dfr = dfr
        
        response.isSignificant = self.is_result_significant(p_value, alpha_value)
            
        # returning the response
        return response

    
    # calculates value of SSR
    def calculate_ssr(self, ycap_arr, ybar):
        ssr = 0
        for item in ycap_arr:
            ssr += self.calc_power(item - ybar,2)
        return ssr
    
    
    # calculates value of SSE
    def calculate_sse(self, y_arr, ycap_arr):
        sse = 0
        for i in range(len(y_arr)):
            sse  += self.calc_power(y_arr[i]-ycap_arr[i],2)    
        return sse

    
    # calculates value of MSE
    def calculate_mse(self, sse, dfe):
        return sse/dfe

    
    # calculates value of MSR
    def calculate_msr(self, ssr, dfr):
        return ssr/dfr

    
    # calculates value of F
    def calculate_f_value(self, msr, mse):
        return msr/mse

    def is_result_significant(self, p_value, alpha_value):
        if p_value < alpha_value:
            return True
        else:
            return False
    
    def calculate_p_value(self, dfr, dfe, f_value):
        return 1 - self.incompbeta(.5*dfr, .5*dfe, float(dfr)*f_value/(dfr*f_value+dfe))
    
    def incompbeta(self, a, b, x):
        if (x == 0):
            return 0;
        elif (x == 1):
            return 1;
        else:
            lbeta = math.lgamma(a+b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1-x)
            if (x < (a+1) / (a+b+2)):
                return math.exp(lbeta) * self.contfractbeta(a, b, x) / a;
            else:
                return 1 - math.exp(lbeta) * self.contfractbeta(b, a, 1-x) / b;

    def contfractbeta(self, a,b,x, ITMAX = 200):
        EPS = 3.0e-7
        bm = az = am = 1.0
        qab = a+b
        qap = a+1.0
        qam = a-1.0
        bz = 1.0-qab*x/qap

        for i in range(ITMAX+1):
            em = float(i+1)
            tem = em + em
            d = em*(b-em)*x/((qam+tem)*(a+tem))
            ap = az + d*am
            bp = bz+d*bm
            d = -(a+em)*(qab+em)*x/((qap+tem)*(a+tem))
            app = ap+d*az
            bpp = bp+d*bz
            aold = az
            am = ap/bpp
            bm = bp/bpp
            az = app/bpp
            bz = 1.0
            if (abs(az-aold)<(EPS*abs(az))):
                return az
        
    # computes f statistics given the regression equation and input array
    # this will act as the main method for computing f-statistics
    def calculate_f_statistic(self, y_arr, y_cap_arr, num_estimated_params, alpha_value):
        if len(y_arr) != len(y_cap_arr):
            raise ValueError('Mismatch in the size of y and y_cap input arrays')

        # computing f-statistics
        dfr = num_estimated_params - 1

        return self.compute_anova(y_arr, y_cap_arr, dfr, alpha_value)

    def compare_and_choose_best_model(self, y_arr, models_arr, alpha_value):
        if len(models_arr) < 2:
            raise ValueError('Need atleast 2 models to compare')
        
        significant_models_array_indexes = []
        significant_models_f_values = []
        
        for i in range(len(models_arr)):
            response = self.calculate_f_statistic(y_arr, models_arr[i].y_cap_arr, models_arr[i].num_estimated_params ,alpha_value)
            
            if response.isSignificant == True:
                significant_models_array_indexes.append(i)
                significant_models_f_values.append(response.f)
            
        # finding max value in significant_models_f_values and return the corresponding index of the model
        max = -1
        max_f_value_model_index = -1
        for i in range(len(significant_models_f_values)):
            if significant_models_f_values[i] > max:
                max = significant_models_f_values[i]
                max_f_value_model_index = i
        
        return max_f_value_model_index